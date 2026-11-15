# SemanticMemory

[![CI](https://github.com/kapildhinwa2010-dev/SemanticMemory/actions/workflows/ci.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/SemanticMemory/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kapildhinwa2010-dev/SemanticMemory/actions/workflows/codeql.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/SemanticMemory/actions/workflows/codeql.yml)


Alias-aware semantic recall: direct hits first, then co-occurrence-ranked related facts.

**Part of the [Kapildhinwa2010-dev Toolkit](https://github.com/kapildhinwa2010-dev/Kapildhinwa2010-dev).**

## What it does

SemanticMemory is the RECALL layer of the fact-tool family. recall()
returns direct hits first, then co-occurrence-ranked related facts;
topics are canonicalized through the same_as alias closure, so a query
for "rob" finds facts stored under "bob". Graph operations live in
KnowledgeGraph; causal analysis in CausalMemory.

## Install

```bash
pip install -r requirements.txt
```

## Quick start

```python
from semanticmemory import KnowledgeNet

net = KnowledgeNet()
net.add("bob", "likes", "tea")
net.add("bob", "same_as", "Robert")
print(net.recall("Robert"))  # finds the tea fact via alias
```

## API

- add / query / facts / chain / interference - shared triple store
- recall(topic, top_k) - direct hits first, then related facts
- related_topics(topic, top_k) - co-occurring topics ranked by count

## Honest results and limitations

- "Semantic" here means co-occurrence counting plus alias expansion -
  no embeddings, no similarity model, no fuzzy matching.
- recall() ranking beyond direct hits is a simple count, ties broken
  alphabetically.
- Alias canonical representative is min() of the group (byte order),
  deterministic but arbitrary in meaning.

## License

MIT - see [LICENSE](LICENSE).
