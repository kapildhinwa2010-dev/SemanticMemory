# SemanticMemory

SemanticMemory is a small Python library for storing string-valued subject–predicate–object facts and retrieving related facts from an in-memory store. It includes exact-pattern queries, transitive `same_as` alias groups, and simple count-based retrieval helpers. The project is at version 0.1.0 and should be treated as an early-stage utility, not a production-ready semantic search system.

## Requirements and installation

The package metadata requires Python 3.9 or newer and declares `numpy>=1.24` as a dependency. From a clone of this repository, install the package with:

```bash
python -m pip install .
```

The package built into a wheel and installed successfully in a temporary target directory during review. For development and tests, install the listed requirements and run pytest:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Basic use

```python
from semanticmemory import KnowledgeNet

memory = KnowledgeNet()
memory.add("bob", "likes", "tea")
memory.add("bob", "same_as", "robert")

# Alias-aware recall can find the fact stored under "bob".
for fact in memory.recall("robert"):
    print(fact.as_tuple())

# Exact pattern query; None leaves a field unrestricted.
for fact in memory.query(subject="bob"):
    print(fact)
```

`add(subject, predicate, object)` accepts non-empty strings and returns `False` when the same triple is already stored. Facts are kept in memory for the lifetime of the `KnowledgeNet` instance; there is no persistence layer.

## Implemented operations

- `facts()` returns all stored facts in tuple-sorted order, and `len(memory)` returns the fact count.
- `query(subject=None, predicate=None, obj=None)` filters by any supplied exact string fields; `None` acts as a wildcard.
- `derive_aliases()` returns the transitive connected groups formed by `same_as` facts. The representative for each group is the lexicographically smallest member; that choice is deterministic but has no semantic meaning.
- `recall(topic, top_k=5)` gathers facts directly mentioning the topic or a member of its `same_as` group. If fewer than `top_k` such facts are available, it adds candidates from `interference()`. The combined results are sorted by their fact tuples before truncation; direct results are not guaranteed to appear first.
- `interference(query, top_k=3)` considers facts that mention the exact query string and ranks them using a count of related subject/object matches. This is a simple heuristic, not a learned relevance score.
- `related_topics(topic, top_k=3)` counts other terms directly co-occurring with the topic or its chosen canonical alias and returns the highest counts, with alphabetical tie-breaking. It does not expand every alias in the group.
- `chain(start, predicate, max_hops=4)` follows matching predicate facts from the start, choosing the first matching outgoing fact encountered at each step and stopping at a missing edge, a repeated node, or the hop limit.

`top_k` must be at least 1 for the ranking methods; `max_hops` must be at least 1 for `chain`.
The repository does not define a command-line interface; use the Python module API.

## Tests and CI

On the reviewed checkout (`d7d3cd0`), `python -m pytest -q` completed locally with **10 passed**. `python -m compileall -q semanticmemory.py tests` also completed successfully, and package installation via `pip install --no-deps --no-build-isolation --target /tmp/readme95-install-check .` succeeded. These are local checks, not a claim about a hosted CI run.

The repository defines a GitHub Actions workflow that runs pytest and a compile/import smoke check on Python 3.10, 3.11, and 3.12. A separate workflow configures CodeQL analysis. Workflow configuration alone does not establish the status of any hosted run. No benchmark results are included.

## Scope and limitations

This is a basic in-memory triple store with exact string matching and small, deterministic helper algorithms. It does not provide embeddings, fuzzy matching, natural-language understanding, persistence, a database backend, a ranking model, or a graph/causal-analysis system. `interference` and `related_topics` use simple counts, while alias representatives are lexicographic rather than user-selected. `chain` follows one encountered outgoing match instead of exploring or returning all possible paths. There is no evidence here of performance benchmarks or production-readiness validation.

## License

The repository includes an MIT License. See [LICENSE](LICENSE) for the full terms and copyright notice.
