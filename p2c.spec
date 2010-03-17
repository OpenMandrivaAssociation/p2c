%define	name	p2c
%define	version	1.22
Summary:	A Pascal to C translator
Name:		%{name}
Version:	%{version}
Release:	%mkrel 17
License:	GPL
Group:		Development/Other
Source0:	ftp://csvax.cs.caltech.edu/pub/p2c-1.22.tar.bz2
URL:		http://www.synaptics.com/people/daveg/
Patch2:		p2c-newpatch.patch
# Fixes conflicting types for 'my_memcpy' build error: thanks Anssi
Patch3:		p2c-1.22-memcpy.patch
Patch4:		p2c-1.22-getline.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

Install the p2c-devel package if you want to do p2c development.

%prep
%setup -q
%patch2 -p1 -b .new
%patch3 -p1 -b .memcpy
%patch4 -p0 -b .getline
mkdir src/shlib
mkdir include
ln -s ../src include/p2c

%build
cp src/sys.p2crc src/p2crc
make RPM_OPTS="$RPM_OPT_FLAGS -fPIC"
make RPM_OPTS="$RPM_OPT_FLAGS -fPIC" shlib -C src

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}{%{_mandir}/man1,%{_prefix}/lib,%{_libdir},%{_includedir}}
make install RPM_INSTALL=%{buildroot} LIBDIR=$RPM_BUILD_ROOT%{_libdir} MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
#%doc %_docdir/p2c-1.22
%{_bindir}/*
%{_libdir}/libp2c.so*
%{_prefix}/lib/p2c
%{_mandir}/man1/p2c.1*

%files devel
%defattr(-,root,root)
%{_libdir}/libp2c.a
%{_includedir}/p2c
