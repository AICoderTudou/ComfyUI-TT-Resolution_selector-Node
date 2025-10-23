"""
ComfyUI TT Resolution Selector Plugin
TT常用分辨率选择插件
"""

from .nodes.resolution_selector import TTResolutionSelector

# 节点映射
NODE_CLASS_MAPPINGS = {
    "TTResolutionSelector": TTResolutionSelector,
}

# 节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "TTResolutionSelector": "TT分辨率选择器",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']