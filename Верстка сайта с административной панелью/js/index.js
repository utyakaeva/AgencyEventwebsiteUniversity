'use strict';

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var CitiesSlider = function (_React$Component) {
  _inherits(CitiesSlider, _React$Component);

  function CitiesSlider(props) {
    _classCallCheck(this, CitiesSlider);

    var _this = _possibleConstructorReturn(this, _React$Component.call(this, props));

    _this.IMAGE_PARTS = 4;

    _this.changeTO = null;
    _this.AUTOCHANGE_TIME = 4000;

    _this.state = { activeSlide: -1, prevSlide: -1, sliderReady: false };
    return _this;
  }

  CitiesSlider.prototype.componentWillUnmount = function componentWillUnmount() {
    window.clearTimeout(this.changeTO);
  };

  CitiesSlider.prototype.componentDidMount = function componentDidMount() {
    var _this2 = this;

    this.runAutochangeTO();
    setTimeout(function () {
      _this2.setState({ activeSlide: 0, sliderReady: true });
    }, 0);
  };

  CitiesSlider.prototype.runAutochangeTO = function runAutochangeTO() {
    var _this3 = this;

    this.changeTO = setTimeout(function () {
      _this3.changeSlides(1);
      _this3.runAutochangeTO();
    }, this.AUTOCHANGE_TIME);
  };

  CitiesSlider.prototype.changeSlides = function changeSlides(change) {
    window.clearTimeout(this.changeTO);
    var length = this.props.slides.length;

    var prevSlide = this.state.activeSlide;
    var activeSlide = prevSlide + change;
    if (activeSlide < 0) activeSlide = length - 1;
    if (activeSlide >= length) activeSlide = 0;
    this.setState({ activeSlide: activeSlide, prevSlide: prevSlide });
  };

  CitiesSlider.prototype.render = function render() {
    var _this4 = this;

    var _state = this.state;
    var activeSlide = _state.activeSlide;
    var prevSlide = _state.prevSlide;
    var sliderReady = _state.sliderReady;

    return React.createElement(
      'div',
      { className: classNames('slider', { 's--ready': sliderReady }) },
      React.createElement(
        'div',
        { className: 'slider__slides' },
        this.props.slides.map(function (slide, index) {
          return React.createElement(
            'div',
            {
              className: classNames('slider__slide', { 's--active': activeSlide === index, 's--prev': prevSlide === index }),
              key: slide.city
            },
            React.createElement(
              'div',
              { className: 'slider__slide-content' },
              React.createElement(
                'h2',
                { className: 'slider__slide-heading' },
                slide.city.split('').map(function (l) {
                  return React.createElement(
                    'span',
                    null,
                    l
                  );
                })
              ),
              React.createElement(
                'span',
                { className: 'slider__slide-readmore'},
                'ПОДРОБНЕЕ'
              )
            ),
            React.createElement(
              'div',
              { className: 'slider__slide-parts' },
              [].concat(Array(_this4.IMAGE_PARTS).fill()).map(function (x, i) {
                return React.createElement(
                  'div',
                  { className: 'slider__slide-part', key: i },
                  React.createElement('div', { className: 'slider__slide-part-inner', style: { backgroundImage: 'url(' + slide.img + ')' } })
                );
              })
            )
          );
        })
      ),
      React.createElement('div', { className: 'slider__control', onClick: function onClick() {
          return _this4.changeSlides(-1);
        } }),
      React.createElement('div', { className: 'slider__control slider__control--right', onClick: function onClick() {
          return _this4.changeSlides(1);
        } })
    );
  };

  return CitiesSlider;
}(React.Component);

var slides = [{
  city: '#незабываемыеднирождения',
  img: 'http://schoolfield.com.ua/assets/images/2015/1/slider03_2.jpg'
}, {
  city: '#лучшиесвадьбыиркутска',
  img:'https://10daily.com.au/ip/s3/2018/08/15/6aa8f9896c398123f1ab1000d756a4df-62544.jpg'
}, {
  city: '#задорныекорпоративы',
  img: 'http://muzfiesta.ru/sites/default/files/photos/34/muzfiesta.ru-121.jpg'
}, {
  city: '#памятныеюбилеи',
  img: 'http://i1.wp.com/www.imenno.ru/wp-content/uploads/2016/02/lIpBm.jpg'
}, {
  city: '#забавныефишки',
  img: 'https://img.fonwall.ru/o/49/noch-salyut-dyim-ogni.jpg'
}];

ReactDOM.render(React.createElement(CitiesSlider, { slides: slides }), document.querySelector('#app'));