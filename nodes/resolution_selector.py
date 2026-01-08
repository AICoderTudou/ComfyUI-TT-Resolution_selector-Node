"""
TT分辨率选择器节点
提供常用分辨率的下拉选择，返回width和height
"""

class TTResolutionSelector:
    """
    TT分辨率选择器节点
    """
    
    # 常用分辨率预设 (名称: (宽度, 高度))
    RESOLUTIONS = {
        "3072x2048 (横屏)": (3072, 2048),
        "2048x3072 (竖屏)": (2048, 3072),
        "640x960 (2:3) (竖屏)": (640, 960),
        "960x640 (3:2) (横屏)": (960, 640),
        "832x1216 (13:19) (竖屏)": (832, 1216),
        "1216x832 (19:13) (横屏)": (1216, 832),
        "1024x1536 (2:3) (竖屏)": (1024, 1536),
        "1536x1024 (3:2) (横屏)": (1536, 1024),
        "1280x720 (16:9) (横屏)": (1280, 720),
        "1920x1080 (16:9) (横屏)": (1920, 1080),
        "720x1280 (9:16) (竖屏)": (720, 1280),
        "1080x1920 (9:16) (竖屏)": (1080, 1920),
        "1344x768 (7:4) (横屏)": (1344, 768),
        "768x1344 (4:7) (竖屏)": (768, 1344),
        "1152x896 (9:7) (横屏)": (1152, 896),
        "896x1152 (7:9) (竖屏)": (896, 1152),
        "480x832 (3:5.2) (竖屏)": (480, 832),
        "832x480 (5.2:3) (横屏)": (832, 480),
        "480x854 (9:16) (竖屏)": (480, 854),
        "854x480 (16:9) (横屏)": (854, 480),
        "512x512 (1:1) (方形)": (512, 512),
        "768x768 (1:1) (方形)": (768, 768),
        "1024x1024 (1:1) (方形)": (1024, 1024),
        "512x768 (2:3) (竖屏)": (512, 768),
        "768x512 (3:2) (横屏)": (768, 512),
        "512x896 (4:7) (竖屏)": (512, 896),
        "896x512 (7:4) (横屏)": (896, 512),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        定义输入类型
        """
        return {
            "required": {
                "use_custom_resolution": ("BOOLEAN", {"default": False, "label_on": "开启自定义", "label_off": "关闭自定义"}),
                "resolution": (list(cls.RESOLUTIONS.keys()), {
                    "default": "1024x1024 (1:1) (方形)"
                }),
                "custom_width": ("INT", {"default": 1024, "min": 64, "max": 8192, "step": 1}),
                "custom_height": ("INT", {"default": 1024, "min": 64, "max": 8192, "step": 1}),
            }
        }
    
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_resolution"
    CATEGORY = "utils"
    
    def get_resolution(self, use_custom_resolution, resolution, custom_width, custom_height):
        """
        根据选择的分辨率返回宽度和高度
        
        Args:
            use_custom_resolution (bool): 是否使用自定义分辨率
            resolution (str): 选择的分辨率字符串
            custom_width (int): 自定义宽度
            custom_height (int): 自定义高度
            
        Returns:
            tuple: (width, height)
        """
        if use_custom_resolution:
            return (custom_width, custom_height)
            
        width, height = self.RESOLUTIONS.get(resolution, (1024, 1024))
        return (width, height)
