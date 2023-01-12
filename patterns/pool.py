class Resource:

    """Some resource, that clients need to use.

    The resources usualy have a very complex and expensive
    construction process, which is definitely not a case
    of this Resource class in my example.
    """

    __value = 0

    def reset(self):
        """Put resource back into default setting."""
        self.__value = 0

    def setValue(self, number):
        self.__value = number

    def getValue(self):
        return self.__value


class ObjectPool:

    """Resource manager.
    Handles checking out and returning resources from clients.
    It's a singleton class.
    """

    __instance = None
    __resources = list()

    def __init__(self):
        if ObjectPool.__instance is not None:
            raise NotImplementedError("This is a singleton class.")

    @staticmethod
    def getInstance():
        if ObjectPool.__instance is None:
            ObjectPool.__instance = ObjectPool()

        return ObjectPool.__instance

    def getResource(self):
        if len(self.__resources) > 0:
            print("Using existing resource.")
            return self.__resources.pop(0)
        else:
            print("Creating new resource.")
            return Resource()

    def returnResource(self, resource):
        resource.reset()
        self.__resources.append(resource)


def main():
    pool = ObjectPool.getInstance()

    # These will be created
    one = pool.getResource()
    two = pool.getResource()

    one.setValue(10)
    two.setValue(20)

    print(one, one.getValue())
    print(two, two.getValue())

    pool.returnResource(one)
    pool.returnResource(two)

    one = None
    two = None

    # These resources will be reused
    one = pool.getResource()
    two = pool.getResource()
    print(f"{one}, {one.getValue()}")
    print(f"{two}, {two.getValue()}")


if __name__ == "__main__":
    main()
