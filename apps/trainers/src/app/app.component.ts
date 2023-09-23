import { Component, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { RouterModule } from '@angular/router';


@Component({
  standalone: true,
  imports: [RouterModule],
  selector: 'org-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'trainers';

  http = inject(HttpClient);

    ngOnInit() {
        this.verifySession();
    }


  verifySession() {
    this.http
      .get('/api/auth/verify-session', {withCredentials: true})
      .subscribe(console.log);
  }
}
