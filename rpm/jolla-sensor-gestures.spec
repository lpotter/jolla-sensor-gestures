# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       jolla-sensor-gestures

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}

Summary:    Sensor gesture plugin for Jolla
Version:    0.1
Release:    2
Group:      Qt/Qt
License:    LICENSE
Source0:    %{name}-%{version}.tar.bz2
Requires:   qt5-qtsensors
Requires:   sailfishsilica-qt5
BuildRequires:  pkgconfig(Qt5Sensors)
BuildRequires:  pkgconfig(Qt5Core)

%description
Sensor gesture plugin for Jolla

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf lib/cmake
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
rm -rf %{buildroot}/lib/cmake
# << install post

%package plugin-gestures-sailfish
Summary:    Sensor gesture plugin for Sailfish
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-gestures-sailfish
This package contains the gesture plugin for SailfishOS

%files

%files plugin-gestures-sailfish
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sensorgestures/libqtsailfishsensorgestures_plugin.so