%define major 0
%define libname %mklibname squeeze %{major}

Summary:	Adavanced archive manager for the Xfce
Name:		squeeze
Version:	0.2.1
Release:	%mkrel 2
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
the Xfce Desktop Environment.
Its design adheres to the Xfce philosophy, which basically 
means Squeeze is both fast and easy to use.

%package -n %{libname}
Summary:	Main library for squeeze
Group:		System/Libraries
	
%description -n %{libname}
Main library for squeeze.

%package -n %{libname}-devel
Summary:	Development files for squeeze
Group:		Development/Other
Provides:	%{name}-devel
Provides:	lib%{name}-devel

%description -n %{libname}-devel
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

desktop-file-install --vendor="" \
    --add-category="X-MandrivaLinux-System-Archiving-Compression" \
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
%{_libdir}/*.so.%{major}*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
