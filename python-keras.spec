Summary:	A deep learning API written in Python
Name:		python-keras
Version:	2.12.0
Release:	1
License:	Expat
Group:		Development/Python
Url:		https://keras.io/
Source0:	https://github.com/keras-team/keras/archive/refs/tags/v%{version}/keras-%{version}.tar.gz
#Source0:	https://pypi.io/packages/source/m/keras/keras-%{version}.tar.gz
BuildRequires:	links

#BuildRequires:	markdown
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(h5py)
BuildRequires:	python%{pyver}dist(keras-applications)
BuildRequires:	python%{pyver}dist(keras-preprocessing)
BuildRequires:	python%{pyver}dist(installer)
BuildRequires:	python%{pyver}dist(nose)
BuildRequires:	python%{pyver}dist(numpy)
#BuildRequires:	python%{pyver}dist(pandas)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	python%{pyver}dist(pip)
#BuildRequires:	python%{pyver}dist(pydot)
BuildRequires:	python%{pyver}dist(python-distutils-extra)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pyyaml)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(scipy)
BuildRequires:	python%{pyver}dist(six)
#BuildRequires:	python%{pyver}dist(tensorboard)
#BuildRequires:	python%{pyver}dist(tensorflow)
BuildRequires:	python%{pyver}dist(theano)
BuildRequires:	python%{pyver}dist(pyyaml)
BuildRequires:	python%{pyver}dist(wheel)

BuildArch:	noarch

%description
Keras is a deep learning API written in Python, running on top of the
machine learning platform TensorFlow. It was developed with a focus on
enabling fast experimentation. Being able to go from idea to result as
fast as possible is key to doing good research.

Keras is:
  - Simple   -- but not simplistic. Keras reduces developer cognitive
                load to free you to focus on the parts of the problem
                that really matter.
  - Flexible -- Keras adopts the principle of progressive disclosure
                of complexity: simple workflows should be quick and
                easy, while arbitrarily advanced workflows should be
                possible via a clear path that builds upon what you've
                already learned.
  - Powerful -- Keras provides industry-strength performance and
                scalability: it is used by organizations and companies
                including NASA, YouTube, or Waymo.

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{py_puresitedir}/docs
%{py_puresitedir}/keras
%{py_puresitedir}/*.*-info/

#-----------------------------------------------------------------------

%prep
%autosetup -c -n keras-%{version}

%build
%py_build

%install
%py_install

