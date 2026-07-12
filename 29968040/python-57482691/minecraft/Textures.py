import GL11
import GLU
from PIL import Image

class Textures:
    idMap: dict = {}

    '''
     * 加载贴图文件
     * @param resourceName
     * @param mode
     * @return
    '''
    @staticmethod
    def loadTexture(resourceName: str, mode: int):
        if resourceName[0] == '/':
            resourceName = resourceName[1:]
        if 1:
        # try:
            if resourceName in Textures.idMap:
                return Textures.idMap[resourceName]

            _id = GL11.glGenTextures(1)
            Textures.idMap[resourceName] = _id
            print(resourceName, "->", _id)

            GL11.glBindTexture(GL11.GL_TEXTURE_2D, _id)

            GL11.glTexParameteri(GL11.GL_TEXTURE_2D, GL11.GL_TEXTURE_MIN_FILTER, mode)
            GL11.glTexParameteri(GL11.GL_TEXTURE_2D, GL11.GL_TEXTURE_MAG_FILTER, mode)

            img = Image.open(resourceName).convert('RGBA')
            w, h = img.size
            pixels = img.tobytes()
            GLU.gluBuild2DMipmaps(GL11.GL_TEXTURE_2D, GL11.GL_RGBA, w, h, GL11.GL_RGBA, GL11.GL_UNSIGNED_BYTE, pixels)

            return _id
        # except:
        #     pass
        raise ValueError
