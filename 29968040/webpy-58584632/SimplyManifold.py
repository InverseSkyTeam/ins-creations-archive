class SimplyManifold:
    def __init__(self,BodyA,BodyB,Normal,Depth,Contact1,Contact2,ContactCount):
        self.BodyA = BodyA
        self.BodyB = BodyB
        self.Normal = Normal
        self.Depth = Depth
        self.Contact1 =Contact1
        self.Contact2 = Contact2
        self.ContactCount = ContactCount