/*!

=========================================================
* Black Dashboard React v1.2.1
=========================================================

* Product Page: https://www.creative-tim.com/product/black-dashboard-react
* Copyright 2022 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/black-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";

// reactstrap components
import {
  Button,
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  CardText,
  FormGroup,
  Form,
  Input,
  Row,
  Col
} from "reactstrap";

function UserProfile() {
  return (
    <>
      <div className="content">
        <Row>
          <Col md="3">
            <Card>
              <CardHeader>
                <h5 className="title">Feeder #1</h5>
              </CardHeader>
              <CardBody>
                <Form>
                  <Row>
                    <Col className="pr-md-1" md="12">
                      <label>Nominal Feeder Capacity</label>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Day</label>
                        <Input
                          defaultValue="0"
                          placeholder="MW"
                          type="text"
                        />
                        <Input
                          defaultValue="0"
                          placeholder="MWh"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                    <Col className="pl-md-1" md="6">
                      <FormGroup>
                        <label>Night</label>
                        <Input
                          defaultValue="0"
                          placeholder="MW"
                          type="text"
                        />
                        <Input
                          defaultValue="0"
                          placeholder="MWh"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="12">
                      <label>Capacity Alarms</label>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Yellow Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                    <Col className="pl-md-1" md="6">
                      <FormGroup>
                        <label>Red Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>                  
                  <Row>
                    <Col className="pr-md-1" md="12">
                      <label>Capacity Alerts</label>
                    </Col>
                  </Row>  
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Capacity</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="4">
                      <label>Price Alarms</label>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Yellow Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                    <Col className="pl-md-1" md="6">
                      <FormGroup>
                        <label>Red Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="4">
                      <label>Price Alerts</label>
                    </Col>
                  </Row>  
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Price</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                </Form>
              </CardBody>
              <CardFooter>
                <Button className="btn-fill" color="primary" type="submit">
                  Set
                </Button>
                <Button className="btn-fill" color="primary" type="submit">
                  Apply to All
                </Button>
              </CardFooter>
            </Card>
          </Col>
          <Col md="3">
            <Card>
              <CardHeader>
                <h5 className="title">Feeder #2</h5>
              </CardHeader>
              <CardBody>
                <Form>
                  <Row>
                    <Col className="pr-md-1" md="12">
                      <label>Nominal Feeder Capacity</label>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Day</label>
                        <Input
                          defaultValue="0"
                          placeholder="MW"
                          type="text"
                        />
                        <Input
                          defaultValue="0"
                          placeholder="MWh"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                    <Col className="pl-md-1" md="6">
                      <FormGroup>
                        <label>Night</label>
                        <Input
                          defaultValue="0"
                          placeholder="MW"
                          type="text"
                        />
                        <Input
                          defaultValue="0"
                          placeholder="MWh"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="12">
                      <label>Capacity Alarms</label>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Yellow Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                    <Col className="pl-md-1" md="6">
                      <FormGroup>
                        <label>Red Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>                  
                  <Row>
                    <Col className="pr-md-1" md="12">
                      <label>Capacity Alerts</label>
                    </Col>
                  </Row>  
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Capacity</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="4">
                      <label>Price Alarms</label>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Yellow Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                    <Col className="pl-md-1" md="6">
                      <FormGroup>
                        <label>Red Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="4">
                      <label>Price Alerts</label>
                    </Col>
                  </Row>  
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Price</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                </Form>
              </CardBody>
              <CardFooter>
                <Button className="btn-fill" color="primary" type="submit">
                  Set
                </Button>
                <Button className="btn-fill" color="primary" type="submit">
                  Apply to All
                </Button>
              </CardFooter>
            </Card>
          </Col>
          <Col md="3">
            <Card>
              <CardHeader>
                <h5 className="title">Feeder #3</h5>
              </CardHeader>
              <CardBody>
                <Form>
                  <Row>
                    <Col className="pr-md-1" md="12">
                      <label>Nominal Feeder Capacity</label>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Day</label>
                        <Input
                          defaultValue="0"
                          placeholder="MW"
                          type="text"
                        />
                        <Input
                          defaultValue="0"
                          placeholder="MWh"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                    <Col className="pl-md-1" md="6">
                      <FormGroup>
                        <label>Night</label>
                        <Input
                          defaultValue="0"
                          placeholder="MW"
                          type="text"
                        />
                        <Input
                          defaultValue="0"
                          placeholder="MWh"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="12">
                      <label>Capacity Alarms</label>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Yellow Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                    <Col className="pl-md-1" md="6">
                      <FormGroup>
                        <label>Red Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>                  
                  <Row>
                    <Col className="pr-md-1" md="12">
                      <label>Capacity Alerts</label>
                    </Col>
                  </Row>  
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Capacity</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="4">
                      <label>Price Alarms</label>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Yellow Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                    <Col className="pl-md-1" md="6">
                      <FormGroup>
                        <label>Red Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="4">
                      <label>Price Alerts</label>
                    </Col>
                  </Row>  
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Price</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                </Form>
              </CardBody>
              <CardFooter>
                <Button className="btn-fill" color="primary" type="submit">
                  Set
                </Button>
                <Button className="btn-fill" color="primary" type="submit">
                  Apply to All
                </Button>
              </CardFooter>
            </Card>
          </Col>
          <Col md="3">
            <Card>
              <CardHeader>
                <h5 className="title">Feeder #4</h5>
              </CardHeader>
              <CardBody>
                <Form>
                  <Row>
                    <Col className="pr-md-1" md="12">
                      <label>Nominal Feeder Capacity</label>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Day</label>
                        <Input
                          defaultValue="0"
                          placeholder="MW"
                          type="text"
                        />
                        <Input
                          defaultValue="0"
                          placeholder="MWh"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                    <Col className="pl-md-1" md="6">
                      <FormGroup>
                        <label>Night</label>
                        <Input
                          defaultValue="0"
                          placeholder="MW"
                          type="text"
                        />
                        <Input
                          defaultValue="0"
                          placeholder="MWh"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="12">
                      <label>Capacity Alarms</label>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Yellow Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                    <Col className="pl-md-1" md="6">
                      <FormGroup>
                        <label>Red Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>                  
                  <Row>
                    <Col className="pr-md-1" md="12">
                      <label>Capacity Alerts</label>
                    </Col>
                  </Row>  
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Capacity</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="4">
                      <label>Price Alarms</label>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Yellow Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                    <Col className="pl-md-1" md="6">
                      <FormGroup>
                        <label>Red Alarm</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-md-1" md="4">
                      <label>Price Alerts</label>
                    </Col>
                  </Row>  
                  <Row>
                    <Col className="pr-md-1" md="6">
                      <FormGroup>
                        <label>Price</label>
                        <Input
                          defaultValue="0"
                          placeholder="Percentage"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                </Form>
              </CardBody>
              <CardFooter>
                <Button className="btn-fill" color="primary" type="submit">
                  Set
                </Button>
                <Button className="btn-fill" color="primary" type="submit">
                  Apply to All
                </Button>
              </CardFooter>
            </Card>
          </Col>
          {/* <Col md="4">
            <Card className="card-user">
              <CardBody>
                <CardText />
                <div className="author">
                  <div className="block block-one" />
                  <div className="block block-two" />
                  <div className="block block-three" />
                  <div className="block block-four" />
                  <a href="#pablo" onClick={(e) => e.preventDefault()}>
                    <img
                      alt="..."
                      className="avatar"
                      src={require("assets/img/emilyz.jpg")}
                    />
                    <h5 className="title">Mike Andrew</h5>
                  </a>
                  <p className="description">Ceo/Co-Founder</p>
                </div>
                <div className="card-description">
                  Do not be scared of the truth because we need to restart the
                  human foundation in truth And I love you like Kanye loves
                  Kanye I love Rick Owens’ bed design but the back is...
                </div>
              </CardBody>
              <CardFooter>
                <div className="button-container">
                  <Button className="btn-icon btn-round" color="facebook">
                    <i className="fab fa-facebook" />
                  </Button>
                  <Button className="btn-icon btn-round" color="twitter">
                    <i className="fab fa-twitter" />
                  </Button>
                  <Button className="btn-icon btn-round" color="google">
                    <i className="fab fa-google-plus" />
                  </Button>
                </div>
              </CardFooter>
            </Card>
          </Col> */}
        </Row>
      </div>
    </>
  );
}

export default UserProfile;
