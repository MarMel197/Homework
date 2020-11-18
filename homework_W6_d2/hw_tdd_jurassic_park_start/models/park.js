const Park = function(parkName, price) {
    this.parkName = parkName;
    this.price = price;
    this.dinosaurs = [];
};

Park.prototype.numberOfDinosaurs = function() {
    return this.dinosaurs.length;
};

Park.prototype.addDinosaur = function(dinosaur) {
    this.dinosaurs.push(dinosaur);
};

Park.prototype.removeDinosaur = function(dinosaur) {
    const indexOfDinosaur = this.dinosaurs.indexOf(dinosaur);
    this.dinosaurs.splice(indexOfDinosaur, 1);
}

Park.prototype.mostVisitors = function() {
    const arrayOfDinosaurs = [];
    for (const currentDinosaur of this.dinosaurs) {
        arrayOfDinosaurs.push(currentDinosaur.guestsAttractedPerDay);
    };

    for (const currentDinosaur of this.dinosaurs) {
        if (Math.max.apply(Math, arrayOfDinosaurs) == currentDinosaur.guestsAttractedPerDay) {
            return currentDinosaur;
        };
    };
};

module.exports = Park;