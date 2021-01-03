<?php

namespace App\Http\Controllers;

use App\Models\Book;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Validator;
use Illuminate\Http\Request;

class BookController extends Controller
{
    public function __construct()
    {
        $this->middleware('auth');
    }

    public function create() {
        return view('books/create');
    }

    public function store() {
        $data = request()->validate([
            'title' => ['required'],
            'author' => ['required'],
            'price' => ['required'],
            'image' => ['required', 'image']
        ]);

        $imagePath = request('image')->store('uploads', 'public');

        auth()->user()->books()->create([
            'title' => $data['title'],
            'author' => $data['author'],
            'price' => $data['price'],
            'image' => $imagePath
        ]);

        return redirect('/profile/'.auth()->user()->id);
    }

}
