%define	pkgname gnuplot

Summary:	Gnuplot scripts for Octave
Name:       octave-%{pkgname}
Version:	1.0.1
Release:       3
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/gnuplot/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 2.9.7
Requires:	gnuplot >= 4.0
BuildRequires:  octave-devel >= 2.9.9
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:	gnuplot >= 4.0
BuildArch:	noarch

%description
This package provides scripts that can save data in gnuplot-readable
formats, specify the gnuplot commands used to produce
graphics, and invoke gnuplot. 

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"
mv %{buildroot}%{_datadir}/octave/packages/%{pkgname}-%{version}/Changelog .
rm -f %{buildroot}%{_datadir}/octave/packages/%{pkgname}-%{version}/COPYRIGHT
rm -f %{buildroot}%{_datadir}/octave/packages/%{pkgname}-%{version}/LICENSE.txt

tar zxf %SOURCE0 
mv %{pkgname}/COPYING .
mv %{pkgname}/DESCRIPTION .

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%doc COPYING DESCRIPTION Changelog
%{_datadir}/octave/packages/%{pkgname}-%{version}
