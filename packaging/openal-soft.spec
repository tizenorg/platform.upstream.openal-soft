Name:           openal-soft
Version:        1.13
Release:        1
License:        LGPL-2.0+
Summary:        A cross-platform 3D audio API
URL:            http://connect.creativelabs.com/openal/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  cmake

%description
OpenAL is a cross-platform 3D audio API appropriate for use with gaming
applications and many other types of audio applications.

%package devel
Summary:        openal-soft development package
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
Development package for OpenAL, a cross-platform 3D audio API
appropriate for use with gaming applications and many other types of
audio applications.

%prep
%setup -q

%build
%cmake .
make %{?_smp_mflags}

%install
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING
%{_bindir}/openal-info
%{_libdir}/libopenal.so.*

%files devel
%{_includedir}/AL/*.h
%{_libdir}/libopenal.so
%{_libdir}/pkgconfig/openal.pc
