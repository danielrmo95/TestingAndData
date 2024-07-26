describe('User Registration', () => {
  beforeEach(() => {
    cy.visit('https://test-qa.inlaze.com/auth/sign-in');
  });

  it('should validate login no password', () => {
    
    cy.get('#email').type('danielrmo95@gmail.com');
    cy.get('button[type="submit"]').should('be.disabled');
  });


  it('should validate login no Email', () => {
    
    cy.get('#password').type('Contrasena1');
    cy.get('button[type="submit"]').should('be.disabled');
  }); 
});




