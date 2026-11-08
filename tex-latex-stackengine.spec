Summary:	Highly customised stacking of objects, insets, baseline changes, etc.
Name:		tex-latex-stackengine
Version:	4.11
Release:	1
License:	LaTeX Project Public License v1.3+
Group:		Applications/Publishing
Source0:	https://mirrors.ctan.org/macros/latex/contrib/stackengine.zip
# Source0-md5:	d08dd166126a0ef5345116e5a14bd264
URL:		https://ctan.org/pkg/stackengine/
BuildRequires:	/usr/bin/latex
BuildRequires:	rpmbuild(macros) >= 1.751
Provides:	tex(stackengine.sty)
Requires(post,postun):	/usr/bin/texhash
# TODO: use generic
Requires:	texlive-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package provides a versatile way to stack objects vertically in a
variety of customizable ways. A number of useful macros are provided,
all of which make use of the stackengine core.

%prep
%setup -q -n stackengine

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{doc,tex}/latex/stackengine

cp -p *.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/stackengine
cp -p *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/stackengine

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc README
%doc %{_datadir}/texmf/doc/latex/stackengine
%{_datadir}/texmf/tex/latex/stackengine
