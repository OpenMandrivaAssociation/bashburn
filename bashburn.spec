%define name bashburn
%define version 3.0.1
%define release %mkrel 6

Summary: Bash script designed to make CD burning
Name: %{name}
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.gz
License: GPL
Group: Archiving/Cd burning
Url: http://bashburn.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: cdrkit, eject, cdrdao, mpg123, vorbis-tools, flac
Buildarch: noarch

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
rm -rf %{buildroot}
./Install.sh --prefix=%buildroot%_prefix

# correct the symlink
ln -sf /usr/lib/Bashburn/lib/BashBurn.sh %{buildroot}%{_bindir}/bashburn
# fix BBROOTDIR in BashBurn.sh:
sed -i -e 's,BBROOTDIR='.*',BBROOTDIR='/usr/lib/Bashburn/lib',' %{buildroot}/usr/lib/Bashburn/lib/BashBurn.sh

%if 0
install -m 755 -D BashBurn.sh %{buildroot}%{_bindir}/BashBurn.sh
pushd %{buildroot}%{_bindir} && %__ln_s BashBurn.sh bashburn && popd
for i in burning/* config/* convert/* lang/English/* menus/* misc/*; do
	install -m 755 -D $i %{buildroot}%{_datadir}/%{name}/$i
done
install -m 644 -D bashburnrc %{buildroot}/etc/bashburnrc
pushd %{buildroot}/etc && %__sed -i "s|BBROOTDIR: .*|BBROOTDIR: /usr/share/bashburn|" bashburnrc && popd
rm -f Install.sh
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/*
%{_bindir}/*
%{_prefix}/lib/Bashburn
#attr(664,root,cdwriter) %config(noreplace) /etc/bashburnrc
%{_datadir}/man/man1/*
