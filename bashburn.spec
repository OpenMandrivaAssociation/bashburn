Summary:	Bash script designed to make CD burning
Name:		bashburn
Version:	3.0.1
Release:	%mkrel 3
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
%if 0
install -m 755 -D BashBurn.sh $RPM_BUILD_ROOT%{_bindir}/BashBurn.sh
pushd $RPM_BUILD_ROOT%{_bindir} && %__ln_s BashBurn.sh bashburn && popd
for i in burning/* config/* convert/* lang/English/* menus/* misc/*; do
	install -m 755 -D $i $RPM_BUILD_ROOT%{_datadir}/%{name}/$i
done
install -m 644 -D bashburnrc $RPM_BUILD_ROOT/etc/bashburnrc
pushd $RPM_BUILD_ROOT/etc && %__sed -i "s|BBROOTDIR: .*|BBROOTDIR: /usr/share/bashburn|" bashburnrc && popd
rm -rf Install.sh
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/*
%{_bindir}/*
%{_prefix}/lib/Bashburn
#attr(664,root,cdwriter) %config(noreplace) /etc/bashburnrc
%{_datadir}/*
