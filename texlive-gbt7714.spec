Name:		texlive-gbt7714
Version:	64633
Release:	1
Summary:	BibTeX implementation of China's bibliography style standard GB/T 7714-2015
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gbt7714
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gbt7714.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gbt7714.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gbt7714.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a BibTeX implementation for the Chinese
national bibliography style standard GB/T 7714-2015. It
consists of two bst files for numerical and author-year styles
as well as a LaTeX package which provides the citation style
defined in the standard. The package is compatible with natbib
and supports language detection (Chinese and English) for each
biblilography entry.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/bibtex/gbt7714
%{_texmfdistdir}/tex/latex/gbt7714
%{_texmfdistdir}/bibtex/bst/gbt7714
%doc %{_texmfdistdir}/doc/bibtex/gbt7714

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
