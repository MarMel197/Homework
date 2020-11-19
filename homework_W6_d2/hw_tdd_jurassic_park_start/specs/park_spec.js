const assert = require('assert');
const Park = require('../models/park.js');
const Dinosaur = require('../models/dinosaur.js');

describe('Park', function() {
  
  let park;
  // Need to do lets for dinosaurs

  beforeEach(function () {
    park = new Park('Jurassic', 14.99);
    let velociraptor = Dinosaur('Velociraptor', 'carnivore', 200);
    let stegasaurus = Dinosaur('Stegasaurus', 'herbivore', 10);
    let spinosaurus = Dinosaur('Spinosaurus', 'carnivore', 100);
  });

  it('should have a name', function() {
    const actual = park.parkName;
    assert.strictEqual(actual, 'Jurassic');
  });

  it('should have a ticket price', function() {
    const actual = park.price;
    assert.strictEqual(actual, 14.99);
  });

  it('should have a collection of dinosaurs', function() {
    const actual = park.dinosaurs;
    assert.deepStrictEqual(actual, []);
  });

  it('should be able to add a dinosaur to its collection', function() {
    park.addDinosaur('Velociraptor')
    const actual  = park.dinosaurs;
    assert.strictEqual(actual, ['Velociraptor']);
  });

  it('should be able to remove a dinosaur from its collection', function(){
    park.addDinosaur('Velociraptor');
    park.addDinosaur('Stegasaurus');
    park.removeDinosaur('Velociraptor')
    const expected = ['Stegasaurus'];
    const actual = park.dinosaurs;
    assert.deepStrictEqual(actual, expected);
  });

  it('should be able to find the dinosaur that attracts the most visitors', function() {
    park.addDinosaur(velociraptor);
    park.addDinosaur(stegasaurus);
    park.addDinosaur(spinosaurus);
    const expected = velociraptor;
    assert.deepStrictEqual(park.mostVisitors(), expected);
  });

  it('should be able to find all dinosaurs of a particular species');

  it('should be able to calculate the total number of visitors per day');

  it('should be able to calculate the total number of visitors per year');

  it('should be able to calculate total revenue for one year');

});
