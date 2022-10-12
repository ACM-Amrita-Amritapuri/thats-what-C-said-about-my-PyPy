using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class button_event_manager : MonoBehaviour
{
    public Button b1 ;
     public Animator animator;

    public Slider slider;
    public Text spdtxt , spdval;
    bool check_settings;

    void Start(){
        check_settings = false;
    }
    public void checkifclickstartbutton(){

        SceneManager.LoadScene("Earth-scene");
    }

    public void checkifclicksettingsbutton(){
        check_settings = !check_settings;

        spdtxt.gameObject.SetActive(check_settings);

        spdval.gameObject.SetActive(check_settings);

        slider.gameObject.SetActive(check_settings);

        animator.SetBool("animate_val",check_settings);

        if(check_settings){
            b1.GetComponentInChildren<Text>().text = "back";
        }else{
            b1.GetComponentInChildren<Text>().text = "settings";
        }
    
        
        

        // SceneManager.LoadScene("settings");
    }

    public void checkifclickback(){

        SceneManager.LoadScene("Main menu");
    }
}
