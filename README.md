# stager
## Stager: An unofficial Gentoo installer designed in C as Thesis Project from ChrisADR

Welcome to stager, an unofficial Gentoo installer designed and developed by ChrisADR.

### Why an unofficial installer?

The [Official Installer Project](https://wiki.gentoo.org/wiki/Project:Installer)is responsible for the design and development of the software. This is a personal project, which is also my thesis project, and is designed to work in C. Most of the official Gentoo software is written in Python, and in order to keep the same language along the project, it would be a better idea to create a python _stager_.

### Why in C language?

This is also a personal choice, given the fact that I don't study C in the institute and I want to be able to demostrate that I know about C programming, I wanted to challenge myself to create a C program that was able to work, and work good. 

## Use cases

Given the multiple configuration cases, stager focuses on the installation of systems based on amd64. It will be designed to follow most sections from the Gentoo Handbook but will ignore some others like internet connection (but will alert the user about that).

Stager needs to accomplish two use cases needed by developers and new users when installin Gentoo.

* They need to be able to create a custom _stage4_ tarball given a current installation.
* They need to be able to create a custom _stage4_ tarball from scratch.
* An optional use case, if I succeed in the first two, will be to have a TUI (Terminal User Interface) to be able to do most of the configuration.

## Dependencies

Stager will depend on these packages and libraries:

* GNU tar

## Contribution

Any kind of contribution/suggestion/question/answer is welcome, so please feel free to create an Issue or even a Pull Request and I'll try to answer as soon as possible.

Thank you.

