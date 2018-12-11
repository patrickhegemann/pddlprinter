from collections import defaultdict


class ObjectSet:
    """
    The set of objects that a planning problem comprises
    """
    def __init__(self):
        # Dictionary with object types as keys and objects as values
        self.objects = set()

    def add(self, obj):
        self.objects.add(obj)

    def get_object_by_name(self, name):
        for o in self.objects:
            if o.name == name:
                return o
        return None

    # def get_by_name(self, name):
    #    for o in self.objects:
    #        if o.name == name:
    #            return o
    #    return None

    def __str__(self):
        # Group objects by type
        objects_by_type = defaultdict(list)
        for o in self.objects:
            objects_by_type[o.object_type.name].append(o.name)

        s = "\t(:objects\n"
        for object_type, obj_list in objects_by_type.items():
            obj_list.sort()
            s += "\t\t%s - %s\n" % (" ".join([str(obj) for obj in obj_list]), object_type)
        s += "\t)\n"
        return s
