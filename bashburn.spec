%define bblib %{buildroot}%{_prefix}

Summary:	Bash script designed to make CD burning
Name:		bashburn
Version:	3.0.1
Release:	%mkrel 5
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
#mkdir -p %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)/usr
mkdir -p %{bblib}
find . -print | cpio -pdum $RPM_BUILD_ROOT/usr/
sed -e "s^@@BBROOTDIR@@^%{bblib}^" %{bblib}/BashBurn.sh > newbb-$$.sh
mv newbb-$$.sh %{bblib}/BashBurn.sh
chmod 755 %{bblib}/BashBurn.sh
mkdir %{buildroot}%{_bindir} 
ln -sf %{bblib}/BashBurn.sh %{buildroot}%{_bindir}/bashburn

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/*
