# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sailfishos-lockscreen-player-patch

# >> macros
BuildArch: armv7hl
# << macros

Summary:    Lockscreen player controls
Version:    0.0.3
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager

%description
Lockscreen player controls


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-lockscreen-player-patch
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-lockscreen-player-patch
mkdir -p %{buildroot}/usr/lib/qt5/qml/org/coderus/mpris
cp -r org/* %{buildroot}/usr/lib/qt5/qml/org
mkdir -p %{buildroot}/usr/share/jolla-settings/pages/sailfishos-lockscreen-player-patch
cp -r settings/*.qml %{buildroot}/usr/share/jolla-settings/pages/sailfishos-lockscreen-player-patch
mkdir -p %{buildroot}/usr/share/jolla-settings/entries
cp -r settings/*.json %{buildroot}/usr/share/jolla-settings/entries/
# << install pre

# >> install post
# << install post

%pre
# >> pre
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-lockscreen-player-patch || true
fi
# << pre

%preun
# >> preun
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-lockscreen-player-patch || true
fi
# << preun

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-lockscreen-player-patch
%{_libdir}/qt5/qml/org/coderus/mpris
%{_datadir}/jolla-settings/entries
%{_datadir}/jolla-settings/pages
# >> files
# << files
