Summary: 	A wxWidgets/wxPython/wxPerl GUI designer
Name: 		wxGlade
Version: 	0.6.3tip20100625
Release:    	7%{?dist}
Source0: 	http://downloads.sourceforge.net/wxglade/%{name}-%{version}.tar.gz
Source1:    wxglade.desktop
Source2:    wxglade.png
License: 	MIT
URL:        http://wxglade.sourceforge.net/
Group: 		Development/Tools
BuildArch: 	noarch
BuildRequires: desktop-file-utils
Requires: 	python >= 2.2
Requires: 	wxPython >= 2.6

%description
wxGlade is a GUI designer written in Python with the popular GUI
toolkit wxPython, that helps you create wxWidgets/wxPython user
interfaces. At the moment it can generate Python, C++, Perl and XRC
(wxWidgets' XML resources) code.

%prep
%setup -q


%build
# nothing to do


%install
# cleanup

# make dirs
install -m 755 -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/%{name}/codegen
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/%{name}/edit_sizers
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/%{name}/icons
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/gtk

# copy files needed at runtime
install -m644 -p *.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m644 -p codegen/*  $RPM_BUILD_ROOT%{_datadir}/%{name}/codegen
install -m644 -p edit_sizers/*  $RPM_BUILD_ROOT%{_datadir}/%{name}/edit_sizers
install -m644 -p icons/*.ico icons/*.png icons/*.xpm  $RPM_BUILD_ROOT%{_datadir}/%{name}/icons
install -m644 -p icons/gtk/*.xpm  $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/gtk
cp -Rp widgets  $RPM_BUILD_ROOT%{_datadir}/%{name}/widgets
find docs -type f -exec chmod 644 {} \;

# make a launcher script
cat > $RPM_BUILD_ROOT%{_bindir}/wxglade <<EOF
#!/bin/bash
exec python %{_datadir}/%{name}/wxglade.py "\$@"
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/wxglade

# install desktop entry
desktop-file-install  \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications         \
  %{SOURCE1}
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -m 644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

# docs symlink
ln -s %{_docdir}/%{name}-%{version}/docs $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

%post
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
update-desktop-database %{_datadir}/applications &>/dev/null || :

%files
%doc docs CHANGES.txt README.txt TODO.txt credits.txt license.txt
%{_bindir}/wxglade
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/applications/*


%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3tip20100625-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.6.3tip20100625-6
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3tip20100625-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3tip20100625-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3tip20100625-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.3tip20100625-2
- recompiling .py files against Python 2.7 (rhbz#623417)

* Fri Jun  25 2010 ZC Miao <hellwolf.misty@gmail.com> - 0.6.3tip20100625-1
- update to tip20100625

* Sun Jun  6 2010 ZC Miao <hellwolf.misty@gmail.com> - 0.6.3tip20091130-2
- update source

* Mon Nov 30 2009 ZC Miao <hellwolf.misty@gmail.com> - 0.6.3tip20091130-1
- update to tip version

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May 24 2008 ZC Miao <hellwolf.misty@gmail.com> - 0.6.3-2
- update to 0.6.3

* Sat Nov 24 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.6.1-1
- update to 0.6.1
- remove docs path patch, add a docs symlink instead

* Thu Jul 19 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.5-6
- 248795 , patch for launch help docs correctly

* Mon Apr 16 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.5-5
- update to fix EVR problem

* Sun Apr 15 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.5-2
- file permissions with install command

* Sun Apr 15 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.5-1
- update to 0.5
- launch script with quoted $@
- name to wxGlade

* Tue Feb 27 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.4.1-3
- Desktop entry do not need version number
- remove some comments

* Sun Feb 25 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.4.1-2
- install icon to hicolor directory
- change name to wxglade
- BuildRequires desktop-file-utils
- remove Application category in desktop file
- remove some macro redefination

* Fri Feb 16 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.4.1-2
- Add missing icons

* Fri Feb 16 2007 ZC Miao <hellwolf.misty@gmail.com> - 0.4.1-1
- update to 0.4.1

* Wed Oct 27 2004 Alberto Griggio <agriggio@users.sf.net> 0.3.5-1
- Updated to version 0.3.5

* Wed Mar 10 2004 Alberto Griggio <agriggio@users.sf.net> 0.3.4-1
- Updated to version 0.3.4

* Wed Mar 10 2004 Alberto Griggio <albgrig@tiscalinet.it> 0.3.2-1
- Updated to version 0.3.2

* Tue Sep 02 2003 Alberto Griggio <albgrig@tiscalinet.it> 0.3.1-1
- Updated to version 0.3.1

* Fri Aug 29 2003 Robin Dunn <robind@alldunn.com> 0.3-5
- Initial version
