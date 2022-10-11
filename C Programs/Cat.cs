using UnityEngine;

public class Cat : MonoBehaviour {

    // Reference to Rigidbody2D component
    private Rigidbody2D rb;

    // dirX variable holds direction value by X axis
    // moveSpeed is move speed
    private float dirX, moveSpeed = 5f;

	// Use this for initialization
	void Start () {

        // Assign Rigidbody2D component to rb variable
        // to get access to it
        rb = GetComponent<Rigidbody2D>();
	}
	
	// Update is called once per frame
	void Update () {

        // Read left or right buttons input and
        // assign its value to dirX variable
        // multiplied by moveSpeed value
        dirX = Input.GetAxisRaw("Horizontal") * moveSpeed;
	}

    private void FixedUpdate()
    {
        // Pass a velocity to Cat's Rigidbody2D component in X axis
        // so Cat moves
        rb.velocity = new Vector2(dirX, rb.velocity.y);
    }
}
