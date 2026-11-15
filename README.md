# SemanticMemory

[![CI](https://github.com/kapildhinwa2010-dev/SemanticMemory/actions/workflows/ci.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/SemanticMemory/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kapildhinwa2010-dev/SemanticMemory/actions/workflows/codeql.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/SemanticMemory/actions/workflows/codeql.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 2.0+](https://img.shields.io/badge/pytorch-2.0+-red.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

**Semantic memory system**

Professional implementation of SemanticMemory for research and production use.

## Installation

```bash
pip install SemanticMemory
```

## Usage

```python
import torch
from semanticmemory import SemanticMemory

module = SemanticMemory(dim=256, hidden_dim=512)
output = module(torch.randn(32, 256))
```

## License

MIT License
