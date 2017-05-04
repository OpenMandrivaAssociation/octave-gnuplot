%define octpkg gnuplot

Summary:	Gnuplot scripts for Octave
Name:		octave-%{octpkg}
Version:	1.0.1
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.0.0
BuildRequires:	gnuplot >= 4.0

Requires:	octave(api) = %{octave_api}
Requires:	gnuplot >= 4.0

Requires(post): octave
Requires(postun): octave

%description
Scripts to save data in gnuplot-readable formats, specify gnuplot commands
that will be used to produce graphics, and call gnuplot.

This package is part of unmantained Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*
#%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING

