%define	oname	BashBurn

Name:		bashburn
Version:	3.1.0
Release:	2
Summary:	Bash script designed to make CD burning
Source:		%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Archiving/Cd burning
Url:		https://bashburn.sourceforge.net/
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
%setup -q -n %{oname}-%{version}

%build
make

%install
rm -rf %{buildroot}
./Install.sh --prefix=%{buildroot}%{_prefix}

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


%changelog
* Mon Jan 09 2012 Andrey Bondrov <abondrov@mandriva.org> 3.1.0-1mdv2012.0
+ Revision: 758774
- Fix sources dir
- New version 3.1.0

* Sun Aug 08 2010 Ahmad Samir <ahmadsamir@mandriva.org> 3.0.1-6mdv2011.0
+ Revision: 567724
- clean spec
- correct the /usr/bin/bashburn symlink, (mdv#60548)
- correct BBROOTDIR in BashBurn.sh (spotted by Udo Rader), (mdv#60548)
- bring back the spec from revision 475312

* Fri Jul 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.0.1-5mdv2011.0
+ Revision: 554137
- Fix install and file list, finally (hope)

* Thu Jun 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.0.1-4mdv2010.1
+ Revision: 549110
- fix launch and installation

* Wed Apr 21 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.0.1-3mdv2010.1
+ Revision: 537480
- Fix URL

* Wed Apr 14 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.0.1-2mdv2010.1
+ Revision: 534691
- don't define name, version, release on top of spec.
- Fix mixed-use-of-spaces-and-tabs.
- clean spec..
- fix licence

* Wed Dec 09 2009 Funda Wang <fwang@mandriva.org> 3.0.1-1mdv2010.1
+ Revision: 475312
- new version 3.0.1

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 2.1.2-5mdv2010.0
+ Revision: 424016
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.1.2-4mdv2009.0
+ Revision: 243164
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.1.2-2mdv2008.1
+ Revision: 170771
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Thu Dec 27 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 2.1.2-1mdv2008.1
+ Revision: 138352
- New release 2.1.2

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 29 2007 Funda Wang <fwang@mandriva.org> 2.1-1mdv2008.0
+ Revision: 45632
- New version


* Fri Mar 09 2007 Lenny Cartier <lenny@mandriva.com> 2.0-1mdv2007.1
+ Revision: 138724
- Update to 2.0

* Fri Dec 29 2006 Lenny Cartier <lenny@mandriva.com> 1.8.5-1mdv2007.1
+ Revision: 102456
- Update to 1.8.5
- Import bashburn

* Wed May 10 2006 Lenny Cartier <lenny@mandriva.com> 1.8.0-1mdk
- 1.8.0

* Wed Mar 01 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.7.1-1mdk
- New release 1.7.1

* Thu Jan 26 2006 Lenny Cartier <lenny@mandriva.com> 1.7-1mdk
- 1.7

* Mon Dec 19 2005 Lenny Cartier <lenny@mandriva.com> 1.6.1-1mdk
- 1.6.1

* Fri Feb 04 2005 Jérémie Lenfant-Engelmann <tocman@gmail.com> 1.5.2.1-1mdk
- version 1.5.2.1

* Thu Nov 25 2004 Jérémie Lenfant-Engelmann <tocman@gmail.com> 1.5.2-1mdk
- version 1.5.2

* Sat Aug 28 2004 Jérémie Lenfant-Engelmann <jlenfant@mandrakesoft.com> 1.5-3mdk
- Fix a bug with xmms playlist

* Thu Aug 26 2004 Tocman <jlenfant@mandrakesoft.com> 1.5-2mdk
- bugs fix (with creating ISOs)

* Sun Aug 22 2004 Tocman <jlenfant@mandrakesoft.com> 1.5-1mdk
- First package

