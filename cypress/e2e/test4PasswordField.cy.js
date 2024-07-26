describe('User Registration', () => {
  beforeEach(() => {
    cy.visit('https://test-qa.inlaze.com/auth/sign-up');
  });

  it('should validate password length requirement', () => {
    cy.get('#full-name').type('Daniel Fernando Romero Ochoa');
    cy.get('#email').type('danielrmo95@gmail.com');

    cy.get('#password').type('bogota');
    cy.get('#confirm-password').type('bogota');

    //Validate that the button does not get enabled if the password is incorrect.
    cy.get('button[type="submit"]').should('be.disabled');

  });

  it('should validate password contains uppercase letter', () => {
    cy.get('#full-name').type('Daniel Fernando Romero Ochoa');
    cy.get('#email').type('danielrmo95@gmail.com');

    cy.get('#password').type('bogotac1');
    cy.get('#confirm-password').type('bogotac1');

    cy.get('button[type="submit"]').should('be.disabled');
  });

  it('should validate password contains lowercase letter', () => {
    cy.get('#full-name').type('Daniel Fernando Romero Ochoa');
    cy.get('#email').type('danielrmo95@gmail.com');

    cy.get('#password').type('BOGOTAC1');
    cy.get('#confirm-password').type('BOGOTAC1');

    cy.get('button[type="submit"]').should('be.disabled');

  });

  it('should validate password contains number', () => {
    cy.get('#full-name').type('Daniel Fernando Romero Ochoa');
    cy.get('#email').type('danielrmo95@gmail.com');

    cy.get('#password').type('Bogotacy');
    cy.get('#confirm-password').type('Bogotacy');

    cy.get('button[type="submit"]').should('be.disabled');

  });


  it('should validate password contains Special characters', () => {
    cy.get('#full-name').type('Daniel Fernando Romero Ochoa');
    cy.get('#email').type('danielrmo95@gmail.com');

    cy.get('#password').type('Bogotac1');
    cy.get('#confirm-password').type('Bogotac1');

    cy.get('button[type="submit"]').should('be.disabled');

  });


  it('should validate password meets all criteria and allow registration', () => {
    cy.get('#full-name').type('Daniel Fernando Romero Ochoa');
    cy.get('#email').type('danielrmo95@gmail.com');

    cy.get('#password').type('Bogotac1.');
    cy.get('#confirm-password').type('Bogotac1.');

    cy.contains('button', 'Sign up').click();
    cy.contains('Successful registration!').should('be.visible');
  });
});




