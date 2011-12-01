%define fontname        nafees-web-naskh
%global fontconf        67-%{fontname}.conf
%define archivename     NafeesWeb
%define archivedate     20080509

Name:           %{fontname}-fonts
Version:        1.2
Release:        5%{?dist}
Summary:        Nafees Web font for writing Urdu in the Naskh script 

Group:          User Interface/X
License:        Bitstream Vera
URL:            http://www.crulp.org/Downloads/NafeesWeb.zip

## NOTE: the original archive is unversioned, so we rename it to add a date stamp
# The Source0 is obtained by doing the following:
# $ wget -S http://www.crulp.org/Downloads/NafeesWeb.zip
# $ mv %{archivename} %{fontname}-%{archivedate}.zip
Source0:        %{fontname}-%{archivedate}.zip

## Fix RHBZ# while not fixed upstream
Source1:        %{fontname}-update-preferred-family.pe
Source2:        67-nafees-web-naskh.conf
Source3:        http://www.crulp.org/software/license/License03.html

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch
Requires:       fontpackages-filesystem
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge

%description

Character based Nafees Web Naskh Open Type Font for writing Urdu in Naskh
script based on Unicode standard. This version has complete support of
Aerabs for Urdu and updated glyphs for Latin characters.
Nafees Web Naskh OTF contains approximately 330 glyphs, including 5 ligatures.


%prep
%setup -q -c
cp %{SOURCE3} .

%build
# Fix RHBZ#490830 while not fixed upstream
%{_bindir}/fontforge %{SOURCE1} %{archivename}.ttf

%install
rm -rf %{buildroot}

#fonts
install -d -m 0755 %{buildroot}%{_fontdir}
install -m 0644 *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
                %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}



%clean
rm -rf %{buildroot}

%_font_pkg -f %{fontconf} *.ttf

%doc License03.html
%dir %{_fontdir}

%changelog
* Thu Jun 24 2010 Pravin Satpute <psatpute@redhat.com> - 1.2-5
- added license file from upstream
- Resolves: bug 606878

* Wed Feb 24 2010 Pravin Satpute <psatpute@redhat.com> - 1.2-4
- adding .conf file
- Resolves: bug 567613

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.2-3.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 11 2009 Mathieu Bridon <bochecha@fedoraproject.org> - 1.2-2
- added comment explaining how the source is obtained (as it is modified from upstream)
- temporary fix for RHBZ#490830 while not fixed upstream

* Sat Apr 11 2009 Mathieu Bridon <bochecha@fedoraproject.org> - 1.2-1
- update to 1.2 release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Bernie Innocenti <bernie@codewiz.org> 1.0-4
- Builddep on fontpackages-devel

* Sun Dec 21 2008 Bernie Innocenti <bernie@codewiz.org> 1.0-3
- Typo: fontdir -> _fontdir

* Sun Dec 21 2008 Bernie Innocenti <bernie@codewiz.org> 1.0-2
- Updated to current Fedora font packaging guidelines

* Sat Sep 15 2007 Bernardo Innocenti <bernie@codewiz.org> 1.0-1
- Initial packaging, borrowing many things from abyssinica-fonts
