export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar(brand = this._brand, motor = this._motor, color = this._color) {
    return new this.constructor(brand, motor, color);
  }
}
