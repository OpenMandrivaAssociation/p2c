%define debug_package %nil

Summary:	A Pascal to C translator
Name:		p2c
Version:	1.22
Release:	30
License:	GPLv2
Group:		Development/Other
Url:		https://www.synaptics.com/people/daveg/
Source0:	ftp://csvax.cs.caltech.edu/pub/p2c-1.22.tar.bz2
Source100:	p2c.rpmlintrc
Patch2:		p2c-newpatch.patch
# Fixes conflicting types for 'my_memcpy' build error: thanks Anssi
Patch3:		p2c-1.22-memcpy.patch
Patch4:		p2c-1.22-getline.patch

%description
P2c is a system for translating Pascal programs into the C language.
P2c accepts input source files in certain Pascal dialects:  HP
Pascal, Turbo/UCSD Pascal, DEC VAX Pascal, Oregon Software Pascal/2,
Macintosh Programmer's Workshop Pascal and Sun/Berkeley Pascal.  P2c
outputs a set of .c and .h files which make up a C program equivalent
to the original Pascal program.  The C program can then be compiled
using a standard C compiler, such as gcc.

Install the p2c package if you need a program for translating Pascal
code into C code.

%package	devel
Summary:	Files for p2c Pascal to C translator development
Group:		Development/Other

%description	devel
The p2c-devel package contains the files necessary for development
of the p2c Pascal to C translation system.

%prep
%setup -q
%autopatch -p1
mkdir src/shlib
mkdir include
ln -s ../src include/p2c

%build
cp src/sys.p2crc src/p2crc
%make RPM_OPTS="%{optflags} -fPIC"
%make RPM_OPTS="%{optflags} -fPIC" shlib -C src

%install
mkdir -p %{buildroot}{%{_mandir}/man1,%{_prefix}/lib,%{_libdir},%{_includedir}}
make install RPM_INSTALL=%{buildroot} LIBDIR=%{buildroot}%{_libdir} MANDIR=%{buildroot}%{_mandir}/man1

%files
%{_bindir}/*
%{_libdir}/libp2c.so.*
%{_prefix}/lib/p2c
%{_mandir}/man1/p2c.1*

%files devel
%{_libdir}/libp2c.a
%{_includedir}/p2c

