import inspect


def strict(func):
    def inner(*args, **kwargs):
        parameters = inspect.signature(func).parameters

        args_values = {}
        pnames = list(parameters)
        
        for i in range(len(args)):
            pname = pnames[i]
            pval = args[i]
            
            args_values[pname] = pval

        for pname, pval in kwargs.items():
            args_values[pname] = pval

        for pname, pval in args_values.items():
            annotation_type = parameters[pname].annotation

            if annotation_type not in [bool, int, float, str]:
                continue

            if isinstance(pval, annotation_type) is False:
                raise TypeError()

        return func(*args, **kwargs)

    return inner
