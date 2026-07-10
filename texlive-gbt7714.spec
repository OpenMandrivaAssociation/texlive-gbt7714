%global tl_name gbt7714
%global tl_revision 79531

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0.0
Release:	%{tl_revision}.1
Summary:	A BibTeX implementation of China National Standard GB/T 7714
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/gbt7714
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gbt7714.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gbt7714.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gbt7714.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(bibtex)
Requires:	texlive(natbib)
Requires:	texlive(url)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a comprehensive and configurable BibTeX
implementation of the Chinese National Standard GB/T 7714, Information
and documentation--Rules for bibliographic references and citations to
information resources. The BibTeX styles included in the package support
both numeric and author-year citation systems, and are fully compatible
with the natbib package for advanced citation commands and formatting.
These styles are designed to automatically detect the language (Chinese
or English) of each bibliographic entry and apply the appropriate
localization. Additionally, the package exposes a range of configuration
options, allowing users to easily adapt the output to the requirements
of specific academic journals or institutions.

