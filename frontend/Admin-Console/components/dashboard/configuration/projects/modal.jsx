import axios from 'axios';
import { Form } from 'reactstrap';
import { MdClose } from 'react-icons/md';
import { useForm } from "react-hook-form";
import "bootstrap/dist/css/bootstrap.min.css";
import { API_BASE_URL, API_PORT } from '../../../../config';
import styles from '../../../../styles/dashboard/settings.module.css';
import { useSpring, animated } from 'react-spring';
import { useState, useRef, useEffect, useCallback } from 'react';


export default function Modal({ showmodal, setshowmodal }) {

  //Enpoints and urls

  const companies_endpoint = 'api/companies';
  const companies_url = `${API_BASE_URL}:${API_PORT}/${companies_endpoint}`;

  const create_projects_endpoint = 'api/project/create';
  const create_projects_url = `${API_BASE_URL}:${API_PORT}/${create_projects_endpoint}`;

  //handling Project management, add project data 
  const { register,
    handleSubmit,
    watch,
    errors
  } = useForm();

  // Css Styling classnames
  const {
    button, modalWrapper, closeModalButton,
    modalContent, form, input, saveprojectbutton, Button, modalinputfields

  } = styles;

  // Pop up modal function
  const modalRef = useRef();

  const animation = useSpring({
    config: {
      duration: 250
    },
    opacity: showmodal ? 1 : 0,
    transform: showmodal ? `translateY(0%)` : `translateY(-100%)`
  });

  const closeModal = e => {
    if (modalRef.current === e.target) {
      setshowmodal(false);
    }
  };

  const keyPress = useCallback(
    e => {
      if (e.key === 'Escape' && showmodal) {
        setshowmodal(false);
        console.log('I pressed');
      }
    },
    [setshowmodal, showmodal]
  );

  useEffect(() => {
    document.addEventListener('keydown', keyPress);
    return () => document.removeEventListener('keydown', keyPress);
  },
    [keyPress]
  );




  //Using a second useEffect to make company calls to API
  //-----------------------------------------------------

  useEffect(() => {
    async function getCompanies() {
      const response = await axios.get(companies_url);
      // const body = await response.json();
      setCompany(response.data.map(({ name }) => ({ id: name, name: name })));
    }
    getCompanies();
  }, []);

  //companies object state

  const [company, setCompany] = useState([]);

  //function to fetch companies from endpoint

  // async function getCompanies() {
  //   // const userdata = JSON.parse(localStorage.getItem("user"))

  //   const response = await axios.get(companies_url);
  //   // const body = await response.json();
  //   setCompany(response.data.map(({ name }) => ({ id: name, name: name })));
  // }
  // getCompanies();

  //--------------------------------------------------------------




  //user object state
  const [email, created_by] = useState("")

  //company object state

  const [CompValue, setCompValue] = useState();



  //function for adding new project 
  const onSubmit = (data = { name, company, description, status, created_by }) => {

    const userdata = JSON.parse(localStorage.getItem("user"));
    console.log(userdata)
    if (userdata) {
      // const foundUser = JSON(userdata)
      created_by(userdata.email)
      console.log('user creating project found')
    }

    console.log('data is ', data)
    axios.post(
      create_projects_url,
      JSON.stringify([
        {
          name: data.name,
          company: 1,
          description: data.description,
          status: data.status,
          // created_by: userdata.email
        }
      ]),
      {
        headers: {
          'Content-Type': 'Application/json',
          'Authorization': `Token ${userdata.tokens.access}`
        }
      })
      .then(resp => {

        // On successful addition of Project 
        console.log(resp)

        if (resp.status == 201 || 200) {

          //store added Project details

          localStorage.setItem('project', resp.data)
          console.log(resp.data)
          window.alert('Project added successfully')
          window.location.reload()

          localStorage.setItem('project', JSON.stringify(resp.data))
        }
        else {
          console.log(resp.data)
        }

      }).catch(err => {
        // alert('Kindly enter valid credentials ', err)
        console.log('Failed to add project', err)
        window.alert('Failed to add project')
        window.location.reload()


      })
    console.log(data);

  }
  // console.log(watch('name'))
  // console.log(errors.name)

  return (
    <>
      {showmodal ? (
        <div onClick={closeModal} ref={modalRef}>
          <animated.div style={animation}>
            <div className={modalWrapper} showmodal={showmodal}>
              <div className={modalContent}>
                <h3>Add A New Project</h3>
              </div>

              <div className={form}>
                <Form onSubmit={handleSubmit(onSubmit)}>

                  <div>
                    <input type="text" id="name" placeholder="Enter Project Name" name="name" className={modalinputfields}
                      ref={register({ required: true, minLength: 5 })} /><br />
                    {errors.name && <span className={styles.link}>Project Name must have at least five characters</span>}<br />
                  </div>

                  <div>
                    <select type="text" className={errors.company && styles.errorInput, styles.modalinputfields}
                      placeholder="Company *"
                      name="company"
                      id="company"
                      value={CompValue}
                      onChange={e => setCompValue(e.currentTarget.value)}

                      ref={register({
                        required: true,
                        // pattern: /^[A-Za-z]+$/i,
                      })}
                    >

                      {company.map(({ id, name, key }) => (
                        <option value={key} key={id} name={name}>
                          {name}
                        </option>))}

                    </select>
                  </div>

                  <div>
                    {/* <label>Project Description</label> */}
                    <textarea cols={23} rows={2} id="description"
                      placeholder="Enter Project Description"
                      name="description"
                      className={modalinputfields}
                      ref={register({ required: true, minLength: 25 })}
                      style={{ height: "60%" }}
                    /><br />

                    {errors.description && <span className={styles.link}>Project Description must have a minimum of at least twenty-five characters</span>}<br />

                  </div>

                  <div>
                    <label style={{ fontSize: "12px", float: "left", paddingRight: "80px" }}>Project Status</label>
                    <select id="projectStatus" name="status" className={modalinputfields}
                      ref={register({ required: true })}
                      style={{ width: "20%" }}
                    >
                      <option value="Active">Active</option>
                      <option value="Inactive">Inactive</option>
                    </select>
                  </div>

                  {/*page breaks*/}

                  <br></br>
                  <br></br>

                  {/*page line*/}

                  <hr style={{ left: "-5%", width: "50%" }}></hr>

                  <div className={Button}>
                    <button type="submit" className={saveprojectbutton} id="addproject" value="submit" name="addproject" >
                      Save Project
                                    </button>
                  </div>

                </Form>
              </div>

              <MdClose className={closeModalButton}
                aria-label='Close modal'
                onClick={() => setshowmodal(prev => !prev)}
              />
            </div>

          </animated.div>
        </div>
      ) : null}

    </>

  );

}

