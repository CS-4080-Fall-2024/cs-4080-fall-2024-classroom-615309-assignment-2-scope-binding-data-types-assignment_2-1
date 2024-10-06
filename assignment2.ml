
(* Using the grammar below show a parse tree and a leftmost derivation for the following statement: A = B * (C * (A + B)) *)

(* Grammar: *)
type statement =
  | Assignment of identifier * expression
  | Expression of expression

and expression =
  | Plus of expression * term
  | Term of term

and term =
  | Mult of term * factor
  | Factor of factor

and factor =
  | Grouping of expression
  | Identifier of string

(* Identifiers *)
let identifiers = ["A"; "B"; "C"]

(* Operators *)
let operators = ['+'; '*'; '=']

(* ----------------- *)

(* Pseudocode for the next problem *)
let u = ref 42
let v = ref 69
let w = ref 17

let add z =
  u := !v + !u + z

let bar fun_ =
  let u = w in
  fun_ !v

let foo x w =
  let v = ref x in
  bar add

let main () =
  foo !u 13;
  Printf.printf "%d\n" !u

(* a. Using Static Scope, what is printed to the screen? *)
(* b. Using Dynamic Scope with Deep Binding, what is printed to the screen?  *)
(* c. Using Dynamic Scope with Shallow Binding, what is printed to the screen? *)

(* --------------------- *)

(* Write a program to solve a Sudoku puzzle *)

(* A sudoku solution must satisfy all of the following rules: 
Each of the digits 1-9 must occur exactly once in each row, each column, and each 3x3 sub-grid. *)

(* Example Board *)
let sudoku_board = [|
  [|5; 3; 0; 0; 7; 0; 0; 0; 0|];
  [|6; 0; 0; 1; 9; 5; 0; 0; 0|];
  [|0; 9; 8; 0; 0; 0; 0; 6; 0|];
  [|8; 0; 0; 0; 6; 0; 0; 0; 3|];
  [|4; 0; 0; 8; 0; 3; 0; 0; 1|];
  [|7; 0; 0; 0; 2; 0; 0; 0; 6|];
  [|0; 6; 0; 0; 0; 0; 2; 8; 0|];
  [|0; 0; 0; 4; 1; 9; 0; 0; 5|];
  [|0; 0; 0; 0; 8; 0; 0; 7; 9|]
|]

(* --------------------- *)

(* Rubik's Cube Problem: Design a data structure to store a cube's state in memory *)

type face = string array array

type cube = {
  front : face;
  back : face;
  left : face;
  right : face;
  up : face;
  down : face;
}

(* Create a function to rotate a layer *)

let rotate_face (f : face) =
  (* Rotate a face 90 degrees clockwise *)
  let size = Array.length f in
  let new_face = Array.make_matrix size size "" in
  for i = 0 to size - 1 do
    for j = 0 to size - 1 do
      new_face.(j).(size - 1 - i) <- f.(i).(j)
    done
  done;
  new_face

