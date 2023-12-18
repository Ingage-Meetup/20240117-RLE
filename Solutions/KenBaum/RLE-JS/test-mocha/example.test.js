var expect = require('chai').expect;
const { doAllTheThings } = require('../src/app');

describe('doAllThings', function () {
    it('doAllTheThings should be true', () => {
        expect(doAllTheThings()).to.be.ok
    }); 
});

