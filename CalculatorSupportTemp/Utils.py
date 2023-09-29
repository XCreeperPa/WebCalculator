
def find_all_subclasses(cls) -> list:
    subclasses = list(cls.__subclasses__())
    for subclass in subclasses:
        # Recursively call to get all subclasses
        subclasses.extend(find_all_subclasses(subclass))
    return subclasses