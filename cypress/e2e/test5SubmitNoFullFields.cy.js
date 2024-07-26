describe('User Registration', () => {
  beforeEach(() => {
    cy.visit('https://test-qa.inlaze.com/auth/sign-up');
  });

  it('should validate submit no names', () => {
    
    cy.get('#email').type('danielrmo95@gmail.com');

    cy.get('#password').type('Bogotac1.');
    cy.get('#confirm-password').type('Bogotac1.');

    //Validate that the button does not get enabled if the password is incorrect.
    cy.get('button[type="submit"]').should('be.disabled');


  });

  it('should validate submit no email', () => {
    cy.get('#full-name').type('Daniel Fernando Romero Ochoa');

    cy.get('#password').type('Bogotac1.');
    cy.get('#confirm-password').type('Bogotac1.');

    cy.get('button.btn.btn-primary').should('not.have.attr', 'disabled');

  });

  it('should validate submit no password', () => {
    cy.get('#full-name').type('Daniel Fernando Romero Ochoa');
    cy.get('#email').type('danielrmo95@gmail.com');

    
    cy.get('#confirm-password').type('Bogotac1.');

    cy.get('button.btn.btn-primary').should('not.have.attr', 'disabled');

  });

  it('should validate submit no confirm password', () => {
    cy.get('#full-name').type('Daniel Fernando Romero Ochoa');
    cy.get('#email').type('danielrmo95@gmail.com');

    cy.get('#password').type('Bogotacy');


    cy.get('button.btn.btn-primary').should('not.have.attr', 'disabled');

  });
});




