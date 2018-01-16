# installer
## installer: an unofficial Gentoo installer designed in Python as thesis project from ChrisADR

Welcome to installer, an unofficial Gentoo installer designed and developed by ChrisADR.

### Why an unofficial installer?

The [Official Installer Project](https://wiki.gentoo.org/wiki/Project:Installer) is responsible for the design and development of the software. This is a personal project, which is also my thesis project, and is designed to work in Python.

### Why in Python language?

Python is the official language from Portage and is used widely among Gentoo developers and users.

## Use cases

Given the multiple configuration cases, installer focuses on the installation of systems based on amd64. It will be designed to follow most sections from the Gentoo Handbook.

installer needs to accomplish two use cases needed by developers and new users when installing Gentoo.

* They need to be able to create a custom _stageX_ tarball given a current installation.
* They need to be able to create a custom _stageX_ tarball from scratch.
* An optional use case, if I succeed in the first two, will be to have a TUI (Terminal User Interface) to be able to do most of the configuration.

## Dependencies and Runtime Dependencies

installer will depend on these packages and libraries:

* GNU tar (runtime)
* Iputils (runtime)
* GNU coreutils (runtime)
* Bash (runtime)
* Util-linux (runtime)
* GNU grep (runtime)
* Ncurses (runtime)

## Contribution

Any kind of contribution/suggestion/question/answer is welcome, so please feel free to create an Issue or even a Pull Request and I'll try to answer as soon as possible.

Thank you.
