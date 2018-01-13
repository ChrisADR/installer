
def begin(args):
    """Begin function starts the interactive tutorial for installing Gentoo Linux.
    Possible args:

    @tui: wheter to display information in TUI or CLI 
    """
    import pym.stager.step1 as step1
    step1.init(args)


def resume(step,args):
    """Resume function resumes the interactive tutorial from a specific step in tutorial.
    Possible args:

    @tui: wheter to display information in TUI or CLI
    """
    if step==1:
        import pym.stager.step1 as step1
        step1.init(args)
    elif step==2:
        import pym.stager.step2 as step2
        step2.init(args)
    elif step==3:
        import pym.stager.step3 as step3
        step3.init(args)
    elif step==4:
        import pym.stager.step4 as step4
        step4.init(args)
    elif step==5:
        import pym.stager.step5 as step5
        step5.init(args)
    elif step==6:
        import pym.stager.step6 as step6
        step6.init(args)
