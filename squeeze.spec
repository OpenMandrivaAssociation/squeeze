%define major 0
%define apiversion 1
%define libname %mklibname %{name}- %{apiversion} %{major}
%define develname %mklibname %{name} -d

Summary:	Adavanced archive manager for the Xfce
Name:		squeeze
Version:	0.2.1
Release:	%mkrel 5
License:	GPL
Group:		Archiving/Compression
Url:		http://squeeze.xfce.org
Source0:	http://squeeze.xfce.org/downloads/%{name}-%{version}.tar.bz2
BuildRequires:	thunar-devel
BuildRequires:	desktop-file-utils
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Squeeze is a modern and advanced archive manager for 
the Xfce Desktop Environment.Its design adheres to the 
Xfce philosophy, which basically means Squeeze is both 
fast and easy to use.

%package -n %{libname}
Summary:	Main library for squeeze
Group:		System/Libraries
Obsoletes:	%mklibname %{name} 0

%description -n %{libname}
Main library for squeeze.

%package -n %{develname}
Summary:	Development files for squeeze
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname %{name}- 1 0 -d

%description -n %{develname}
Development files for squeeze.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

desktop-file-install \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog NEWS TODO COPYING
%doc %{_datadir}/gtk-doc/html/*
%{_bindir}/squeeze
%{_libdir}/thunar-archive-plugin/squeeze.tap
%{_datadir}/applications/squeeze.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_datadir}/pixmaps/squeeze/*.png

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*%{apiversion}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
