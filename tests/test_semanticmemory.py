import pytest
import torch
from semanticmemory import SemanticMemory, create_semanticmemory

class TestSemanticMemory:
    def test_init(self):
        m = SemanticMemory(dim=256, hidden_dim=512)
        assert m.dim == 256
    
    def test_forward(self):
        m = SemanticMemory(dim=256)
        x = torch.randn(32, 256)
        assert m(x).shape == (32, 256)
    
    def test_factory(self):
        m = create_semanticmemory()
        assert isinstance(m, SemanticMemory)

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
