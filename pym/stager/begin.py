import pym.stager.walkthrough as walkthrough 


def init(args):
    """The init function takes args from main program and parses them.

    Possible args:
    
    @step: wheter to select a specific installation step
    """
    if args.step != 0:
        walkthrough.resume(args.step,args)
    else:
        walkthrough.begin(args)
