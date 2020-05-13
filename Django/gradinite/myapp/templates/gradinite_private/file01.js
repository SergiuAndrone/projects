
"use strict";

let dict = (a = "black", b) => ({a, b});

let dict1 = dict("red", 15);
let dict2 = dict("blue", 22);

class Car {
  constructor(types, color, engine = "gas") {
    this.types = types;
    this.color = color;
    this.engine = engine;
    console.log("car type: " + this.types);
    console.log("car color: " + this.color);
  }

  engineType() {
    console.log("the type of the engine is: " + this.engine);
  }


}

let bmw = new Car("sport", "red");
bmw.engineType();

const mmm = () => {
  console.log("this is a func");
}
mmm();

export {mmm};

