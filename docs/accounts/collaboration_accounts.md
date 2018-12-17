# Collaboration Accounts

## Overview

Most NERSC login accounts are associated with specific individuals and
must not be shared. Sometimes it is advantageous to have a login
account which is not tied to a person but instead to the group for the
purposes of shared access to batch jobs or data. Collaboration
Accounts are designed to facilitate collaborative computing by
allowing multiple users to use the same account.  All actions
performed by the collaboration account are traceable back to the
individual who used the collaboration account to perform those actions
via gsisshd accounting logs. PIs and PI Proxies can request a
collaboration account by logging into nim and selecting "Request a
Collaboration Account" under the blue "Actions" tab.

## Logging Into Collaboration Accounts

To access your collaboration account on Cori or Edison, login to any
interactive node:

```
collabsu <collaboration account name>
<enter nersc password at the prompt>
```

On the DTN nodes, you must still use the old method using your NERSC
grid certificate. You can also do this on from any PDSF interactive
node, edisongrid, or corigrid (to access corigrid, you must first log
into cori.nersc.gov) as yourself and then do the following commands:

```
module load globus
myproxy-logon -s nerscca.nersc.gov
gsissh localhost -l <project account name>
```

If you're setting the port to 22 in your .ssh/config file, you may also
need to add a "-p 2222" flag to the gsissh command.

Alternatively you can get a proxy using grid-proxy-init instead of
myproxy-logon. In this case you use your GRID pass phrase instead of
your NIM password.

## Controlling Collaboration Account Access

PIs and PI Proxies can give users in their repo access to the
collaboration account by adding them in NIM to the corresponding
group. Each collaboration account has a linux file group associated
with it with the name c_<collaboration account\>. You can add users to
the corresponding group following the instructions
[here](https://www.nersc.gov/users/accounts/nim/nim-guide-for-pis/#toc-anchor-8).

To use the old gsissh method, you must associate their grid
certificate with the account. Log into nim.nersc.gov and click on the
repo with the collaboration account you wish to change. Then click on
the "Project Access" tab in the yellow bar partway down the page. This
will bring you to a page with a pull down menu where you can select
project account and the user you wish to give access to it. If you
encounter any errors with this, please open a ticket with NERSC
consulting.  

## Use Cases

### Collaborative Data Management

Large scale experimental and simulation data are typically read or
written by multiple collaborators and are kept on disk for long
periods. A problem that often arises is that the files are owned by
the collaborator who did the work and if that collaborator changes
roles the default unix file permissions usually are such that the
files cannot be managed (deleted) by other members of the
collaboration and system administrators must be contacted. While the
problem can be addressed with the appropriate use of unix groups and
file permissions in practice this tends to be problematic and a more
seamless solution would be of great utility.

### Collaborative Software Management

The issue with managing software is similar to that of managing data –
different collaborators often need to work with the same files in a
particular software installation and unix groups and file permissions
tend to be problematic for them.  The main difference between
collaborative data and software management is that software is
typically managed on a short-tem basis (hours/days) and smaller in
size (~GBs) whereas production data is managed on a long-term basis
(months/years) and much larger (~TBs to ~PBs).

### Collaborative Job Management

Production level jobs are often run by a small team of collaborators.
Project accounts would enable members of the team to manipulate jobs
submitted by other team members as necessary.