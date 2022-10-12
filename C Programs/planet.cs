using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class planet : MonoBehaviour
{
    public bool clicked;

    public bool clicked_settings;

    public Dropdown dpdown;

    int dpval;
    public Button b1,b2;

    Rigidbody rb;

    string texture = "Sun";

    Renderer rend;

    public Slider speed;
    public Text slidtext;
    public Animator animator;
    
    public void when_button_clicks()
    {
        clicked = !clicked;
        animator.SetBool("animate_val",clicked);
    }
    void Start(){
        rend = gameObject.GetComponent<Renderer>();
        transform.localScale = new Vector3(1.52104f,1.375872f,1.52104f);
    }
    void Update(){
        
        rend.material.mainTexture = Resources.Load(texture) as Texture;
        // print(GameObject.Find("Button").GetComponentInChildren<Text>());
        slidtext.text = speed.value.ToString();
        if(clicked){
            b1.GetComponentInChildren<Text>().text = "pause";
            gameObject.transform.Rotate(0,speed.value,0);
        }else{
            b1.GetComponentInChildren<Text>().text = "play";
        }
    }
    public void dropdown(){
        switch(dpdown.GetComponent<Dropdown>().value){
            case 0:
                texture = "sun";
                break;
            case 1:
                texture = "moon";
                break;
            case 2:
                texture = "mercury";
                break;
            case 3:
                texture = "venus";
                break;
            case 4:
                texture = "earth";
                break;
            case 5:
                texture = "mars";
                break;
            case 6:
                texture = "jupiter";
                break;
            case 7:
                 texture = "saturn";
                break;
            case 8:
                texture = "neptune";
                break;
        }
        setscale(texture);
    }

    void setscale(string texture){
        if(texture=="sun"){
            transform.localScale = new Vector3(1.52104f,1.375872f,1.52104f);
        }else if(texture=="moon"){
            transform.localScale = new Vector3(0.767665744f,0.694399714f,0.767665744f);
        }else if(texture=="jupiter"){
            transform.localScale = new Vector3(1.17180192f,1.05996513f,1.17180192f);
        }else{
            transform.localScale = new Vector3(0.9967225f,0.9015954f,0.9967225f);
        }
    }

}   
