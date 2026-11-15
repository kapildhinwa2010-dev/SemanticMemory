import pytest

from semanticmemory import Fact, KnowledgeNet


def test_fact_basic():
    fact = Fact("alice", "knows", "bob")
    assert fact.as_tuple() == ("alice", "knows", "bob")


def test_add_and_len():
    net = KnowledgeNet()
    assert net.add("a", "knows", "b") is True
    assert len(net) == 1


def test_query_pattern():
    net = KnowledgeNet()
    net.add("a", "knows", "b")
    net.add("a", "likes", "c")
    assert len(net.query(subject="a")) == 2


def test_derive_aliases_transitive():
    net = KnowledgeNet()
    net.add("x", "same_as", "y")
    net.add("y", "same_as", "z")
    aliases = net.derive_aliases()
    assert aliases["x"] == aliases["y"] == aliases["z"]


# --- semantic recall (SemanticMemory-specific) ---


def test_recall_direct_hits():
    net = KnowledgeNet()
    net.add("bob", "works_at", "acme")
    net.add("bob", "likes", "tea")
    facts = net.recall("bob", top_k=5)
    tuples = {f.as_tuple() for f in facts}
    assert ("bob", "works_at", "acme") in tuples
    assert ("bob", "likes", "tea") in tuples


def test_recall_uses_aliases():
    net = KnowledgeNet()
    net.add("bob", "same_as", "robert")
    net.add("robert", "works_at", "acme")
    tuples = {f.as_tuple() for f in net.recall("bob")}
    assert ("robert", "works_at", "acme") in tuples


def test_recall_falls_back_to_interference():
    net = KnowledgeNet()
    net.add("hub", "knows", "a")
    net.add("hub", "knows", "b")
    facts = net.recall("a", top_k=3)
    tuples = {f.as_tuple() for f in facts}
    assert ("hub", "knows", "a") in tuples


def test_recall_rejects_bad_top_k():
    net = KnowledgeNet()
    net.add("a", "knows", "b")
    with pytest.raises(ValueError):
        net.recall("a", top_k=0)


def test_related_topics_ranked():
    net = KnowledgeNet()
    net.add("bob", "knows", "alice")
    net.add("bob", "knows", "carol")
    net.add("bob", "likes", "tea")
    topics = net.related_topics("bob", top_k=2)
    assert topics[0] in {"alice", "carol"}
    assert len(topics) == 2


def test_related_topics_unknown():
    net = KnowledgeNet()
    net.add("a", "knows", "b")
    assert net.related_topics("zzz") == []