Summary:	Bash script designed to make CD burning
Name:		bashburn
Version:	3.0.1
Release:	%mkrel 4
Source:		%name-%{version}.tar.gz
License:	GPLv2+
Group:		Archiving/Cd burning
Url:		http://bashburn.dose.se/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	cdrkit, eject, cdrdao, mpg123, vorbis-tools, flac
Buildarch:	noarch

%description
Sick of all those fancy CD-burning apps not working for you? You need something
that just gets the work done? Welcome to BashBurn - It just works!

BashBurn is the new name for the cd burning shell script Magma. It's not the
best looking CD-burning application out there, but it does what you want it to
do. (And if not then probably didn't want to do it anyway)

Bashburn could need lame codec for some operations.

%prep
%setup -q 

%build
make

%install
rm -rf $RPM_BUILD_ROOT
./Install.sh --prefix=%buildroot%_prefix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/*
%{_bindir}/*
%{_prefix}/lib/Bashburn
#attr(664,root,cdwriter) %config(noreplace) /etc/bashburnrc
%{_datadir}/*
